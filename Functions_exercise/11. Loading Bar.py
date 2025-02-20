loading_bar_procent = int(input()) # 0 - 100

def calculate_loading_bar(a):
    calculate = a // 10
    procent = (calculate * "%")
    dots = ((10 - calculate) * ".")

    if loading_bar_procent < 100:
        print(f'{loading_bar_procent}% [{procent}{dots}]')
        print("Still loading...")
    elif loading_bar_procent == 100:
        print(f'{loading_bar_procent}% Complete!')
        print("[%%%%%%%%%%]")


calculate_loading_bar(loading_bar_procent)