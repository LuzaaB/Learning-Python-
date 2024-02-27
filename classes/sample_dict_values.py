from sample_dict import SampleClass

print(f"Class attribute : {SampleClass.class_attr}")
print(f"Using __dict__ with class attribute : {SampleClass.__dict__}")
print(f"Example of __dict__ : {SampleClass.__dict__["class_attr"]}")

instance = SampleClass("Hello!")
print(f"Instance attribute : {instance.instance_attr}")
print(instance.method())
print(f"Using __dict__ wtih instance instance attribute : {instance.__dict__}")
print(f"Example of __dict__ with instance variable : {instance.__dict__["instance_attr"]}")

instance.__dict__["instance_attr"] = "Hello, Python"
print(instance.instance_attr)