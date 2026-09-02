import matplotlib.pyplot as plt

class VisualDashboard:
    def __init__(self):
        plt.ion()
        self.fig, self.ax = plt.subplots()

        self.rpm_text = self.ax.text(
            0.5,
            1,
            "RPM: 0",
            transform=self.ax.transAxes,
            ha="center",
            va="top"
        )

        plt.show()

    def update(self, rpm):
        self.rpm_text.set_text(f"RPM: {rpm}")
        self.fig.canvas.draw_idle()
        plt.pause(0.01)

if __name__ == "__main__":
    dashboard = VisualDashboard()

    dashboard.update(800)
    plt.pause(2)

    dashboard.update(4000)
    plt.pause(2)

    dashboard.update(8000)

    plt.ioff()
    plt.show()