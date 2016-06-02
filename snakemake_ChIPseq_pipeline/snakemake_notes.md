
see a [post](https://groups.google.com/forum/#!topic/snakemake/iDnr3PIcsfE)  

>Apart from the rule declarations, Snakefiles are plain Python. In your return statement in myfunc, you take the value of the wildcards   
object and put braces around it. Braces around an object in Python create 
a set containing that object. But you just want the value, without wrapping it in a set. Hence, the solution is to remove the braces. 

You should put `{}` around the wildcards within quotes, like so
`"{wildcards.kittens}"`

If you are using wildcards within code you do not need the curly braces, so you can just do 
for kitten in wildcards.kittens:
    print(kitten)
    
