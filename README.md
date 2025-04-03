# IHFC Heat Flow Vocabularies

This repository contains SKOS (Simple Knowledge Organization System) vocabularies relevant to scientific study of Earth's heat flow. Initial development of the vocabularies was supported by the international heat flow community as part of the restructuring of the Global Heat Flow Database and are used for the determination of heat flow data and metadata quality.

## Vocabularies

The following vocabularies are included in the data `data` directory of this repository:

### Heat Flow

- `heat flow method`: Describes the method used to determine heat flow.
- `probe type`: Describes the type of probe used to measure heat flow.
- `transfer method`: Describes the method used to transfer heat flow data.
- `exploration method`: Describes the method used to explore for heat flow.
- `exploration purpose`: Describes the purpose of an exploration for heat flow.
- `geographic environment`: Describes the geographic environment in which heat flow was measured.

### Temperature

- `temperature correction`: Describes the correction applied to a temperature measurement.
- `temperature method`: Describes the method used to determine temperature.

### Thermal Conductivity

- `conductivity location`: Methods used to calculate thermal conductivity in rock specimens or sections for the purpose of heat flow measurements.
- `conductivity method`: Methods used to calculate thermal conductivity in rock specimens or sections for the purpose of heat flow measurements.
- `conductivity PT conditions`: Conditions under which the thermal conductivity are measured.
- `conductivity PT function`: Describes the function used to determine thermal conductivity as a function of pressure and temperature.
- `conductivity saturation`: Describes the saturation state of the material for a thermal conductivity measurement.
- `conductivity source`: Methods used to correct temperature data for the purpose of heat flow measurements.
- `conductivity strategy`: Strategy by which thermal conductivity for a particular heat flow interval was calculated.

### Other

- `correction flags`: Describes flags used to indicate corrections applied to data.

## Contributing

Contributions to this repository are welcome. Please use the issue tracker to discuss any proposed changes before submitting a pull request.

This package relies on the fledgling [skos-builder](https://github.com/SamuelJennings/skos-builder) package, which is a Python library for defining SKOS vocabularies in a declarative and Pythonic way. `skos-builder` is still in early development so bugs should be expected in this package.

## Installation Guide

### Prerequisites

Ensure you have the following installed on your system:

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/) (Ensure it's compatible with the repository requirements)
- [Poetry](https://python-poetry.org) (these instructions assume version**&lt;2.0**)

    You can check your Poetry version with:

        poetry --version

### Installation Steps

1. **Clone the repository**

        git clone https://github.com/ihfc-iugg/ihfc-vocabularies.git

2. **Navigate to the project directory**

        cd ihfc-vocabularies

3. **Install dependencies using Poetry**

        poetry install

    This will create a virtual environment and install all dependencies defined in `pyproject.toml`.

4. **Activate the virtual environment** (if not automatically activated by Poetry)

        poetry shell

5. **Verify the installation**

    Run the following command to check if the package is correctly installed:

        poetry show

## Commands

This guide provides an overview of commonly used commands for managing translations and exporting vocabularies.

### Building vocabularies

    invoke build --format <format>

Builds vocabularies in the specified format (default .ttl).

### Create a New Translation

    invoke new-translation --lang <language_code>

Creates a new translation file for the specified language.

The `lang` argument requires a two-letter ISO 639-1 code (e.g., `fr` for French, `de` for German, etc.).

### Update Existing Translations

    invoke update-translations

Updates all existing translation files with newly extracted messages.

### Compile Translations

    invoke compile-translations

Compiles all translation files into binary format for use in the application.

## Attribution

This repository, along with any code or data, is maintained by the [German Research Centre for Geosciences](https://www.gfz-potsdam.de/en/) (GFZ) via the [World Heat Flow Database Project](heatflow.world) (Deutsche Forschungsgemeinschaft (DFG) - Project number 491795283).

## License

All vocabularies in this repository are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). For more information, see the [data/LICENSE](LICENSE) file.

The codebase for this repository is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.
