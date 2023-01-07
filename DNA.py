import matplotlib.pyplot as plt
from collections import Counter
from mpl_toolkits.mplot3d import Axes3D

class DNA:
    def __init__(self, filename, start=3):
        self.type = "DNA"
        self.header = ""
        self.genomeseq = ""
        self.genome_seq_len = 0
        self.direction(start)
        self.read_FASTA(filename)

    def read_FASTA(self, filename):
        with open(filename) as f:
            fasta_content = f.read()
            for genome in fasta_content.split(">")[1:]:
                self.header, self.genomeseq = genome.splitlines()[0], "".join(genome.splitlines()[1:])
                self.genome_seq_len = len(self.genomeseq)

    def direction(self, start):
        if start == 3:
            self.start, self.finish = 3, 5
        elif start == 5:
            self.start, self.finish = 5, 3

    def c_gc_skewness(self, piece_seq_len=50):
        gc_skew_list = [0]
        for i in range(0, self.genome_seq_len, piece_seq_len):
            genome = self.genomeseq[i:i + piece_seq_len]
            counts = Counter(genome)
            g_count, c_count = counts["G"], counts["C"]
            try:
                skew = (g_count - c_count) / (g_count + c_count)
            except ZeroDivisionError:
                skew = 0
            gc_skew_list.append(gc_skew_list[-1] + skew)
        plt.plot(range(0, len(gc_skew_list)), gc_skew_list)
        plt.show()

    def c_at_skewness(self, piece_seq_len=50):
        at_skew_list = [0]
        for i in range(0, self.genome_seq_len, piece_seq_len):
            genome = self.genomeseq[i:i + piece_seq_len]
            counts = Counter(genome)
            a_count, t_count = counts["A"], counts["T"]
            try:
                skew = (a_count - t_count) / (a_count + t_count)
            except ZeroDivisionError:
                skew = 0
            at_skew_list.append(at_skew_list[-1] + skew)
        plt.plot(range(0, len(at_skew_list)), at_skew_list)
        plt.show()

    def CpG_func(self, piece_seq_len=50):
        cpg_content_list = []
        for i in range(0, self.genome_seq_len, piece_seq_len):
           