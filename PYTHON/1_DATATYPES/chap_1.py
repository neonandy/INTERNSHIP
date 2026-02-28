
#OBJECTs in Python

#mutable and 

spice_mix = set()

print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix id: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("Cardomom")
print(f"Initial spice mix id: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")

"""
the whole point is ~
 
     *the value cannot be changeble - {spice_mix = set()} 

    *the reference can changeble 

        spice_mix.add("Ginger")
        spice_mix.add("Cardomom") can change to ("Lemon") ~
        after this the "spice_mix = set()" VALUE remains same
           
             """

