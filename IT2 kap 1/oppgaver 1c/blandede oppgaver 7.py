def the_first_n_instances_of_the_fibonacci_sequence(n=int):
    fibonaccitall_prev = 0
    fibonaccitall = 1
    fibonaccitall_next = fibonaccitall_prev + fibonaccitall
    print(fibonaccitall)
    for i in range(n - 1):
        fibonaccitall_prev = fibonaccitall
        fibonaccitall = fibonaccitall_next
        fibonaccitall_next = fibonaccitall_prev + fibonaccitall
        print(fibonaccitall)


the_first_n_instances_of_the_fibonacci_sequence(
    int(input("How many iterations of the fibonacci sequence would you like: "))
)
