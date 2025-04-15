#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
nums = []
index1 = index2 = 0
for a in range(0,5):
    nums.append(float(input("Digite um numero\n"))) 
maior = menor = nums[0]
for a in range(0,len(nums)):
    if maior < nums[a]:
        maior = nums[a]
        index1 = a
    if menor > nums[a]:
        menor = nums[a]
        index2 = a
print(f"O maior numero digitado foi {maior} que ocupa a posicao {index1} da lista\nO menor numero digitado foi {menor} que ocupa a posicao {index2} da lista")
print(nums)