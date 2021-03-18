from ortools.graph import pywrapgraph

def main():
    start_nodes = [0, 0, 1, 1, 2, 3] #başlangıç düğümleri    0 düğümü S0, 
    end_nodes =   [1, 2, 3, 2, 4, 4] #bitiş düğümleri        4 düğümü Si'yi temsil ediyor
    capacities =  [2, 3, 4, 3, 2, 1] #düğüm kapasiteleri

    max_flow = pywrapgraph.SimpleMaxFlow()
    for i in range(0, len(start_nodes)):
        max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])
    
    #0 düğümü ile 4 düğümü arasındaki optimumu maksimum akışı bul
    if max_flow.Solve(0, 4) == max_flow.OPTIMAL:
        print('Max flow:', max_flow.OptimalFlow())
        print('------------------------')
        print('  Arc    Flow / Capacity')
        for i in range(max_flow.NumArcs()):
            print('%1s -> %1s   %3s  / %3s' % (
            max_flow.Tail(i),
            max_flow.Head(i),
            max_flow.Flow(i),
            max_flow.Capacity(i)))
    else:
        print('There was an issue with the max flow input.')

if __name__ == '__main__':
    main()