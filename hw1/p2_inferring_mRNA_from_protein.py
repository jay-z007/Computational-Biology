from mapping_helper import *


class Inferring_mRNA(object):
    """Base class for protein related functions"""

    def num_mRNA(self, protein):
        ans = len(protein_2_mRNA["STOP"])

        for i in protein:
            ans *= len(protein_2_mRNA[i])
            ans %= 1000000

        return ans


s = Inferring_mRNA()
#print s.num_mRNA("MA")
#print s.num_mRNA("MASDPHPKPPCLQSAMTTDLWWFFDWIIIGEKKQGKKAFSASSCAFVNDHWNLQRNFPKNRMDRVWEESDLRSSCPPELDFQSHMPTERTKKFPQINGMNCMHVENCENFAVLFQGTAVYYVWCHHKMCSIQQQPSMYEQAMSPDVLLCRSADSMMGKYEWDWSRMVWNVHTKEDNCPMNDKIWALRECCGFGTQAVETQRYVLYWGQMLWHMYESPMVFLYISQDAETLVELLGSQYKHFYKNPQNLFAINGHHQYLTKFMKVKVRSDCSKKKVKTWAMMGEMMSDTFRMNAANIIKGQEYKRFKIYTMESHRALWPMNRQKLCMGHWIRIHFQDWFGYCISITNKPHYQNSCWFDYYMHRGVLTCGLQTSPQHALMDIQNCKMCDCQHYHESGQIPLQWTCVNLFNSDCWADATPWYELQGIKCLYYMYEQKLYFTKGHLQEHWFSHNCMAHQLEITEFKWGMGANFFIFQGELVSAHCVINLRWNNILFRSHRTGYFGWDLWVIMTWWYAQCEFAISGSESITWTLMWSRPFYGYDERRWWIAMPWVCMFNEEWSCNNRMTWTFGHSMSNGFVLAMGYRVKAMNCVRYTSQCNQFCHPDRDFRLVFERMEKMFVQDWYCSADFETRKIYWDWYKAGTLTTYQMPHANLHPFAHWDHSLSFERCMDQMSECRKRWPHSRNDNMRSWHVIYEHCGCQTWGGSPGNVVDGPNWRRWICACVMHIKNWHEDSCVMCWLFHTCHYKVRLNAQPPSHRDGTMQIMMARCPRLIFGKAQSLPGGMMMDPKWVLWCFVFKVFCPAHYPLYIEVIQFLRGRFPRCAQDCLAELEFKTAPYHEHKVQTWRYHAVASAWSRDNVKQPAAIIQWKAAVMLHHCYSRQIVYHFRQWSSCIQHCYLVYVPYRYREFAFEMPTMMTQDTETMWYKDFDIDLVPWHGVNHIVEQDNAEWNNSTCPKRCSHKMVAQDFCETMSHYDDWIHKFWKRDDTVPPKRWFMLNAAS")
