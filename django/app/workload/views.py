from django.http import HttpResponse
import time
import math
import asyncio


async def no_load(request):
    return HttpResponse("nothing to do")


async def sleep(request):
    await asyncio.sleep(1)
    return HttpResponse("sleeping")


async def prime_number(request):
    max_number = 50000
    primes =[]
    for n in range(3, max_number + 1):
        for i in range(2, int(math.sqrt(n) +1)):
            if (n % i) == 0:
                break
        else:
            primes.append(str(n))

    return HttpResponse(",".join(primes))