from ortools.graph import pywrapgraph


def solution():
    start_nodes = [0, 0, 1,2, 2, 3,3,4,5]  #başlangıç düğümleri
    end_nodes =   [1, 2, 3,3, 4, 5,6,5,6]  #bitiş düğümleri 
    capacities =  [6, 7, 3, 5, 4, 4,2,5,8] #düğüm kapasiteleri

    max_flow = pywrapgraph.SimpleMaxFlow()
    for i in range(0, len(start_nodes)):
        max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])
    
    #0 düğümü ile 6 düğümü arasındaki maksimum akışı bul
    if max_flow.Solve(0, 6) == max_flow.OPTIMAL:
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
    solution()