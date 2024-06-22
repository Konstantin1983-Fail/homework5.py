immutable_var = (1, 2, 'a', 'b')
print("Immutable tuple:",immutable_var)

# Следующая строка вызовет ошибку, так как кортежи неизменяемы
# immutable_var[0] = 10
# Кортежи являются неизменяемыми объектами, что означает, что их элементы нельзя изменить после создания.
# Если попытаться изменить элемент кортежа, возникнет ошибка TypeError.

mutable_list = [1, 2, 'a', 'b']
mutable_list[0] = 10
mutable_list.append('Modified')
print("Mutable list", mutable_list)