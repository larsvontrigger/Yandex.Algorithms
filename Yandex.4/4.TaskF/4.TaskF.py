def productlist():
    productlist = {}
    while True:
        datas = str(input())
        if datas.lower() == 'stop':
            break
        name,product,num = map(str,datas.split())
        num = int(num)
        print(productlist)
        if name in productlist:
            if product in productlist[name]:
                productlist[name][product] += num
            else:
                productlist[name][product] = num
        else:
            productlist[name] = {product:num}
    def output():
        for name, products in productlist.items():
            print(f"{name}:")
            for product,num in products.items():
                print(f'{product} {num}')
    output() 
productlist()