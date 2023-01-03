names = open('doc/names.txt', 'w')
name = 'Vasya'
names.write(f"{name}\n")
names.close()

add_names = open('doc/names.txt', 'a')
add_new_name = 'Ivan'
add_names.write(f"{add_new_name}\n")
add_names.close()

read_names = open('doc/names.txt', 'r')
read_name = read_names.read()
print(read_name)
read_names.close()

read_write_names = open('doc/names.txt', 'r+')
add_and_read_new_name = 'Sergey'
read_write_names.write(add_and_read_new_name)
read_write_names.close()

read_names = open('doc/names.txt', 'r')
read_name = read_names.read()
print(read_name)
read_names.close()