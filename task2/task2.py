""""
a) What is the performance, in terms of, Big O notation, of the below code?
 - O(n^2) because of the nested domain.keys() > domain.values()
b) Write a solution that has better performance
c) What is the performance of your new solution?
 - getBlockPolicyStateN() has O(n) time complexity

 def getBlockPolicyState(domains: Dict) -> Dict:
    policyArr = []
    numDomains = len(domains.keys())  # O(n)
    for x in range(numDomains):  # O(n)
        policy = domains.values()[x]["policy"]  # O(n) needs conversion to list on Python3
        policyArr.append(policy)  # O(1)
    oneDomain = [True for policy in policyArr if policy == "block"]  # O(n)
    allDomains = all(policy == "block" for policy in policyArr)  # O(n)
    return dict(oneDomain=oneDomain, allDomains=allDomains)  # O(k)

"""
from typing import Dict

task2 = {
    "one.com": dict(policy="block"),
    "two.com": dict(policy="none"),
    "three.com": dict(policy="none"),
    "four.com": dict(policy="block")
}


def getBlockPolicyState(domains: Dict) -> Dict:
    """ Updated version with O(n) time complexity """
    domain_values = domains.values()  # O(n)
    oneDomain = [True for domain in domain_values if domain.get("policy") == "block"]  # O(n)
    allDomains = len(domain_values) == len(oneDomain)  # O(1)
    return dict(oneDomain=oneDomain, allDomains=allDomains)  # O(k)


print(getBlockPolicyState(task2))
