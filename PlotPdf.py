import matplotlib.pyplot as plt

class PlotPdf:
    def plot_data(self, t, filtered_A, g, title, start=None, end=None):
        plt.figure(figsize=(10, 12))

        plt.subplot(2, 1, 1)
        plt.plot(t, filtered_A, 'g', label='Aceleracion')
        plt.plot(t, g, 'b', label='Aceleracion gravitacional')
        plt.grid(True)
        plt.title(title)
        plt.legend()

        if start is not None and end is not None:
            plt.subplot(2, 1, 2)
            plt.plot(t[start:end], filtered_A[start:end], 'g', label='Aceleracion')
            plt.plot(t[start:end], g[start:end], 'b', label='Aceleracion gravitacional')
            plt.grid(True)
            plt.title('Aceleración con cortes')
            plt.legend()

        plt.tight_layout()
        self.pdf_pages.savefig()

    def plot_velocity(self, t, Vt, title):
        plt.figure()
        plt.plot(t, Vt * 100)
        plt.grid(True)
        plt.title(title)
        if self.output_format == 'pdf':
            self.pdf_pages.savefig()
        else:
            plt.show()

    def close(self):
        if self.pdf_pages:
            self.pdf_pages.close()