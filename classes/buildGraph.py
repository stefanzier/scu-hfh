import csv
import classes.option as opts

def get_options(graph):
    list_options = []
    with open("csv1.csv", 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')

        for row in data:
            index = int(row[0])
            text = row[1]
            option_type = int(row[2])
            add_info_flag = int(row[3])
            next_nodes = row[5].split("|")

            for node in next_nodes:
                graph.add_edge((index, int(node)))


            t_opts = (index, opts.Option(index, text, next_nodes, add_info_flag))
            list_options.append(t_opts)

    return dict(list_options)
