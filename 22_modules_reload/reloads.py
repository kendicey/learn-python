import importlib
import sample
import filechanges

# # import statement will only run once no matter when many times you type it
# import sample
# import sample
# import sample
# import sample

# # importlib.reload() runs the import statement again as you call it
# importlib.reload(sample)
# importlib.reload(sample)
# importlib.reload(sample)

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass

for i in range(5):
    changes()
    input("Hit enter to reload...")