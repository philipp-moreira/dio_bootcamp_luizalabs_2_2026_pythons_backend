### Observations

When working in a scenario where it's necessary to apply abstraction from the real world through classes, especially using the object-oriented programming pillar, Inheritance, I observed that it's not explicitly necessary to create a specialized constructor in the child class(es) if the characteristic attributes don't differ between the classes in the hierarchy (parent class x child class).

Implicitly, the interpreter will identify this at the time of instantiation of the child class and, at runtime, pass the arguments to satisfy the constructor of the parent (super) class.

The constructor of the child class(es) is only necessary when there's a need to "specialize" the attributes of the child class, whether it's:

- specialized characteristics of the child class

- overriding behavior, reusing and complementing the behavior (method/function) of the parent (superior) classes;

It is important to note that this is the moment of decision, when we consider the direction of development through the lens of [SOLID principles](https://en.wikipedia.org/wiki/SOLID) , and especially the Liskov Substitution Principle, because the creation of a subsidiary class, or specialization, particularly in behavior, should not impact current consumers in the upper classes.
