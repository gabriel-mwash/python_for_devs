def least_likely(sub_atomic_particles: dict) -> str:
    """return the sub atomic particle that is the least likely to be observed"
    >>> least_likely({"proton":0.2, "muon":0.03})
    >>> "muon"
    """
    probabilities = list(sub_atomic_particles.values())
    least_probable = min(probabilities)
    for key in sub_atomic_particles:
        if sub_atomic_particles[key] == least_probable:
            return key



if __name__ == "__main__":
    print(least_likely({"proton": 0.2, "muon": 0.03})
          )
        
    
