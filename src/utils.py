def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper
@log_calls
def top_k(scores: dict[str, float], k: int):
    sor = sorted(scores.items(), key=lambda pair : pair[1], reverse = True)
    res = sor[:k]
    return [pair[0] for pair in res]
    
print(top_k({"apple": 3, "pear": 5, "kiwi": 4}, 2))
