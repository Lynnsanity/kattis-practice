guests = int(input())

name_fun_list = []
fun_list = []
for x in range(guests):
    name, fun = input().split(' ')
    fun_int = int(fun)
    name_fun_list.append(name)
    name_fun_list.append(fun)
    fun_list.append(fun_int)

fun_list.sort()

highest_fun = str(fun_list[-1])

index_of_name = int(name_fun_list.index(highest_fun)) - 1
print(name_fun_list[index_of_name])
