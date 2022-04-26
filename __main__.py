from ddosguard import DDOSGuard

ddosguard = DDOSGuard()

if __name__ == "__main__":
    anidex = ddosguard.get("https://anidex.info/").text
    print(anidex)
