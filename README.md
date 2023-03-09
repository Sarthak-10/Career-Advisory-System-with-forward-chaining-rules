# Career-Advisory-System-with-forward-chaining-rules

This project makes use of the durable-rules module of python to create a career advisory system. The career advisory system uses forward chaining rules to advise the best careers for the individual.

You can read more about the durable-rules module [here](https://github.com/jruizgit/rules)

You can find sample runs of the ipynb file in the report attached.

**About Forward Chaining**

In forward chaining we are given a set of basic facts and we try to derive a conclusion from these facts.

For example :-

**Knowledge Base**

IF lion(x) THEN mammal(x)

IF mammal(x) THEN animal(x)

**Fact**

lion(Sam)

Now applying forward chaining to this fact we can conclude that Sam is an animal.

You can read more about forward chaining [here](https://www.javatpoint.com/forward-chaining-and-backward-chaining-in-ai)
