class SampleClass:
    class_attr = 100
    
    def __init__(self, instance_attr):
        self.instance_attr = instance_attr
    
    def method(self):
        print(f"Class attribute : {self.class_attr}")    
        print(f"Instance attribute : {self.instance_attr}")
        
        
# Values
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