import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

z = [1.527, 1.870, 2.098, 4.758, 18.294]

x = [1, 2, 3, 4, 5]

y = [3.5596055075975633E-97, 1.7951858408067537E-67, 5.5907850924339506E-42, 1.979841075573553E-33, 1.7992544067761122E-22]

plt.plot(z, y, "bo")
plt.plot(z, y, "b")

plt.title("Concurrent Path Builder Preliminary Result")

plt.ylabel("Rare-event Probability")
plt.yscale("log")

plt.xlabel("Execution Time (s)")

plt.grid(color='gainsboro', axis='y')


plt.savefig('plot.png')

with PdfPages(r'plot.pdf') as export_pdf:
    export_pdf.savefig()

plt.show()
