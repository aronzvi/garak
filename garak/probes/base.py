#!/usr/bin/env python3

from colorama import Fore, Style
from tqdm import tqdm


class Probe:
    def __init__(self):
        self.name = None
        self.description = "Empty probe"
        self.uri = ""
        self.bcp47 = None  # language this is for, in bcp47 format; * for all langs
        self.recommended_detector = ["toxicity.ToxicCommentModelDetector"]
        probename = str(self.__class__).split("'")[1]
        print(
            f"loading {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}probe: {Style.RESET_ALL}{probename}"
        )

    def probe(self, generator):
        # attempt to exploit the target, return list of results
        results = []
        for prompt in tqdm(self.prompts):
            results += generator.generate(prompt)
        return results


class TextProbe(Probe):
    def __init__(self):
        super().__init__()
        self.prompts = []

    def probe(self, generator):
        return super().probe(generator)
