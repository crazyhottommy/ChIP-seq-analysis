#! /usr/bin/env python

__author__ = 'tommy'

# check the tutorial here https://pythonhosted.org/trackhub/tutorial.html
# import the components we'll be using
# 01/12/2016

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--hub_name", help="Required. the name of your track hub")
parser.add_argument("--base_url", help="Required. the path to the folder where the files are accessible from a web, "
                                       "make sure add the trailing slash")
parser.add_argument("--input_dir", help="Required. the folder where the files are stored in your local computer")
parser.add_argument("--output_dir", help="the folder where the hub track files are generated, default is "
                                         "the same as input_dir", default=".")
parser.add_argument("--email", help="Required. your email to contact")
parser.add_argument("--composite_track_name", help="Required. the name of your composite track")

args = parser.parse_args()

assert args.hub_name is not None, "please provide the hub_name"
assert args.base_url is not None, "please provide the base_url"
assert args.composite_track_name is not None, "please provide the composite track name"
assert args.email is not None, "please provide your email"
assert args.input_dir is not None, "please provide the path to the bigwig and bigbed files on your local computer"


from trackhub import Hub, GenomesFile, Genome, TrackDb

hub = Hub(
    hub='%s' % args.hub_name,
    short_label='%s' % args.hub_name,
    long_label='%s ChIP-seq hub' % args.hub_name,
    email='%s' % args.email)

genomes_file = GenomesFile()
genome = Genome('hg19')
trackdb = TrackDb()

# Bottom-up
genome.add_trackdb(trackdb)
genomes_file.add_genome(genome)
hub.add_genomes_file(genomes_file)

# make a composite track
from trackhub import CompositeTrack

composite = CompositeTrack(
    name="%s" % args.composite_track_name,
    short_label="%s" % args.composite_track_name,
    long_label=" %s ChIP-seq" % args.composite_track_name,
    tracktype="bigWig")

# After the composite track has been created, we can incrementally add additional parameters.
# This is same method can be used for all classes derived from Track CompositeTrack, ViewTrack
# and of course Track itself:

composite.add_params(dragAndDrop='subtracks', visibility='full')

# The next part of the hierarchy is a ViewTrack object. Both ViewTrack and CompositeTrack are subclasses of the more generic Track class,
# so they act in much the same way. This should look familiar, but a notable difference is the addition of the view kwarg
from trackhub import ViewTrack

bed_view = ViewTrack(
    name="bedViewTrack",
    view="Bed",
    visibility="squish",
    tracktype="bigBed 3",
    short_label="beds",
    long_label="Beds")

signal_view = ViewTrack(
    name="signalViewTrack",
    view="Signal",
    visibility="full",
    tracktype="bigWig 0 10000",
    short_label="signal",
    long_label="Signal")

# Add these new view tracks to composite:

composite.add_view(bed_view)
composite.add_view(signal_view)


# We can make changes to the created views without having to add them again to the composite.
# For example, here we add configureable on to each view and print composite to make sure the changes show up:


for view in composite.views:
    view.add_params(configurable="on")


## add the bigwig files and bed files to the track

import os
import glob
from trackhub import Track

os.chdir("%s" % args.input_dir)
# A quick function to return the number in the middle of filenames -- this
# will become the key into the subgroup dictionaries above
# def num_from_fn(fn):
    #return os.path.basename(fn).split('.')[0].split('-')[-1]

# Make the bigBed tracks

def make_bigBed_tracks(bed_view, url_base):
    for bb in glob.glob('*.bigBed'):
        basename = os.path.basename(bb)
        label = bb.replace('.bigBed', '')
        track = Track(
            name='peak_%s' % label,
            tracktype='bigBed 3',
            url=url_base + basename,
            local_fn=bb,
            shortLabel='peaks %s' % label,
            longLabel='peaks %s' % label)

        # add this track to the bed view
        bed_view.add_tracks(track)

# Make the bigWig tracks

def make_bigWig_tracks(signal_view, url_base):
    for bw in glob.glob('*.bw'):
        label = bw.replace('.bw', '')
        basename = os.path.basename(bw)
        track = Track(
            name='signal_%s' % label,
            tracktype='bigWig',
            url=url_base + basename,
            local_fn=bw,
            shortLabel='signal %s' % label,
            longLabel='signal %s' % label)

        # add this track to the signal view
        signal_view.add_tracks(track)

make_bigBed_tracks(bed_view, args.base_url)
make_bigWig_tracks(signal_view, args.base_url)
trackdb.add_tracks(composite)

print trackdb

os.chdir('%s' % args.output_dir)

results = hub.render()

