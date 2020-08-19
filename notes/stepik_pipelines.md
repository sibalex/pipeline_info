*Workflows и Pipelines*

Для сравнения эффективности программ, осуществляющих поиск[ генетических вариантов](https://en.wikipedia.org/wiki/Single-nucleotide_polymorphism), разработана следующая схема анализа данных:
![Image: https://ucarecdn.com/508eddd8-8f4e-45b8-9f66-624d69546f24/](https://ucarecdn.com/508eddd8-8f4e-45b8-9f66-624d69546f24/)

Схема отражает следующий процесс:

1. Исходные данные – результаты [секвенирования](https://en.wikipedia.org/wiki/DNA_sequencing), каждому результату соответствует файл BAM.
2. Для дальнейшего анализа требуется для каждого файла BAM создать файл индекса (BAI).
3. При анализе данных требуется файл с [референсным геномом](https://en.wikipedia.org/wiki/Reference_genome) (общий для всех образцов). Для того, чтобы можно было работать с ним,  требуется создать файл с индексом референса (FAIDX) и словарем [контигов](https://en.wikipedia.org/wiki/Contig) (DICT).
4. Для файла с данными генерируется файл с генетическими вариантами. Для этого используются программы, которые называются [variant callers](https://en.wikipedia.org/wiki/SNV_calling_from_NGS_data). В рамках одного пайплайна может использоваться несколько variant caller'ов.
5. После получения файлов с генетическими вариантами необходимо сравнить между  собой варианты, полученные с использованием разных variant caller'ов.  Процесс сравнения выполняется программой vcf-isec, результат не зависит  от порядка, в котором были взяты файлы, файлы сравниваются попарно
6. variant caller принимает на вход только один файл с данными,  сравнение variant caller'ов нужно провести для каждого из файлов с  результатами секвенирования

Напишите код на Python,  который вычисляет количество шагов, необходимых для анализа n образцов,  где под каждым шагом подразумевается запуск какой-либо программы.  Переменными являются число образцов, которые необходимо проанализировать и количество variant caller'ов (программ генерации вариантов).

Ввод: число образцов для анализа и число variant caller'ов (два целых числа, разделенных пробелом)

Вывод: количество шагов, которые нужно совершить для выполнения анализа (целое число)

​            **Sample Input:**          

```
11 1
```

​            **Sample Output:**          

```
24
```



--

```
n, v = map(int, input().split())
print(2 + n * (1 + v + v * (v - 1) // 2))
```

--

```
print((lambda x,y: 2+x*(1+((y*(y+1))>>1)))(*map(int,input().split(' '))))
```

--

```
def stepik_gen_vars(n, caller):
    if caller <= 2:
        return 2 + n + (n * caller)
    return 2 + n + (n * caller) + (n * caller * (caller - 1) / 2)


if __name__ == '__main__':
     a, b = map(int, input().split())
     print(int(stepik_gen_vars(a, b)))
```

--

```
# put your python code here
bims,vcs = map(int,input().split())
print(bims*(1+vcs)+((vcs*(vcs-1))//2)*bims+2)
```

--

```
from math import factorial

def comb(n):
    return factorial(n) / (2 * factorial(n - 2)) if b >= 2 else 0

a, b = (int(x) for x in input().split())
print(int(2 + a + a * b + a * comb(b)))
```
--
```
countObjects, countVarinCallers = map(int, input().split())

if countVarinCallers <= 2:
    ans = 2 + countObjects + countObjects * countVarinCallers
else:
    ans = 2 + countObjects + countObjects * countVarinCallers + countObjects * countVarinCallers* (countVarinCallers-1) / 2
    
print(int(ans))
```
