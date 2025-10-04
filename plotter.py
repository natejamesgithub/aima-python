import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualizer:
    @staticmethod
    def plot_graph(graph_obj):
        """
        Plot a GraphPlan graph with levels alternating between state and action nodes.
        Left-to-right layout, edges show applicability (state → action).
        """
        G = nx.DiGraph()

        # Assign positions explicitly for left-to-right layout
        pos = {}
        x_offset = 0
        y_spacing = 1.5  # vertical spacing

        for i, level in enumerate(graph_obj.levels):
            # Place states at even i, actions at odd i
            y_offset = 0
            if i % 2 == 0:  # state layer
                for j, state in enumerate(level.current_state):
                    node_id = f"S{i}_{j}"
                    G.add_node(node_id, label=str(state), type="state")
                    pos[node_id] = (x_offset, -j * y_spacing)

                # connect to actions in this level
                for action, preconds in level.current_action_links.items():
                    act_id = f"A{i}_{str(action)}"
                    if act_id not in G:
                        G.add_node(act_id, label=str(action), type="action")
                        pos[act_id] = (x_offset + 1.5, -len(G.nodes) * 0.1)

                    # draw edges from preconditions to this action
                    for pre in preconds:
                        for sid, attrs in G.nodes(data=True):
                            if attrs.get("label") == str(pre):
                                G.add_edge(sid, act_id)

            x_offset += 3  # shift to the right for next level

        # Draw
        node_colors = [
            "skyblue" if data["type"] == "state" else "lightgreen"
            for _, data in G.nodes(data=True)
        ]
        nx.draw(
            G,
            pos,
            with_labels=True,
            labels=nx.get_node_attributes(G, "label"),
            node_size=2000,
            node_color=node_colors,
            font_size=8,
            arrows=True,
            arrowsize=10,
        )

        plt.title("GraphPlan Levels")
        plt.show()