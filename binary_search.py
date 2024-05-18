def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iters = 0

    while low <= high:
        iters += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return mid
    try:
        while arr[mid] < x:
            mid += 1
            iters += 1
    except IndexError:
        return -1
    while arr[mid] > x and mid >= 0:
        mid -= 1
        iters += 1

    return (iters, arr[mid + 1])


rl = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

num = binary_search(rl, 0.01)
print(num)
