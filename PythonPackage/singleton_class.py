class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

					
class MakeSingle(metaclass=Singleton):
	def __init__(self):
		print("I am in init")		
if __name__ == "__main__":
	make = MakeSingle()
	make2 = MakeSingle()			