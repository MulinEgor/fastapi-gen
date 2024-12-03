from core.service import GeneratorService


if __name__ == "__main__":
    options = GeneratorService.get_options()
    GeneratorService(options).generate()
    