MAX = 20
item_weight = int(input("Item weight:\n"))
package = 0
total_weight_sent = 0
current_package_weight = 0
package_num = 0
unsend = 0
unsend_max = 0
wast_pasckage = 0
total_unsend = 0 

while item_weight != 0:
    if 11 > item_weight >0:
        currnet_package_weight += item_weight
        total_weight_sent += item_weight

        if current_package_weight > MAX:
            package_num += 1
            unsend = MAX + item_weight - current_package_weight
            total_unsend += unsend
            current_package_weight = item_weight
            
            if unsend >= unsend_max:
                unsend_max = unsend
                wast_pasckage = package_num
            
        print(f"total weight in current package: {current_package_weight}, package number:{package_num}, unsend: {unsend}")
        print(f"total weight of pasckages sent: {total_weight_sent}, total unsent:{total_unsend}")
        item_weight = int(input("Item weight:\n"))
    else:
        print("invalid item weight!")
        item_weight = int(input("New item weight:\n"))

print(f"Number of package sent: {package_num}.")
print(f"Total weight of package sent: {total_weight_sent}.")
print(f"Total unsend capacity: {total_unsend}.")
print(f"Package number {wast_pasckage} has the most unsend capacity of {unsend_max}")