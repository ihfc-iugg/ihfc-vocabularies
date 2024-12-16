from rdflib.namespace import SKOS
from skos_builder.core import Collection, Concept, ConceptScheme, SKOSBuilder
from skos_builder.translate import gettext as _

BASE_URL = "https://heatflow.world/vocabularies/"
BASE_PREFIX = "ihfc"


class BaseMeta:
    namespace_separator = "#"
    prefix = BASE_PREFIX
    base_url = BASE_URL


class HeatFlowMethod(SKOSBuilder):
    """Methods used to determine heat flow."""

    fourier = Concept(
        {
            SKOS.prefLabel: _("Fourier's Law"),
            SKOS.definition: _(
                "Product of the mean thermal gradient to the mean thermal conductivity with reference to a specified depth interval"
            ),
        },
    )

    product = Concept(
        {
            SKOS.prefLabel: _("Product method"),
            SKOS.definition: _(
                "Product of the mean thermal gradient to the mean thermal conductivity with reference to a specified depth interval"
            ),
        }
    )

    interval = Concept(
        {
            SKOS.prefLabel: _("Interval method"),
            SKOS.definition: _(
                "Product of the mean thermal gradient to the mean thermal conductivity with reference to a specified depth interval"
            ),
        }
    )

    bullard = Concept(
        {
            SKOS.prefLabel: _("Bullard method"),
            SKOS.definition: _(
                "Heat-flow value given as the angular coefficient of the linear regression of the thermal resistance vs. temperature data (used when there is a significant variation of thermal conductivity within the depth range over which the temperatures have been measured)"
            ),
        }
    )

    bootstrap = Concept(
        {
            SKOS.prefLabel: _("Boot-strapping method"),
            SKOS.definition: _(
                "Iterative procedure aimed at minimize the difference between the measured and modelled temperatures by solving the 1-D steady-state conductive geotherm (radiogenic heat production of rocks is accounted for)"
            ),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other"),
            SKOS.definition: _("Specify the method in comments"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Heat flow methods"),
                SKOS.definition: _("Methods used to determine heat flow."),
            }
        )


class ProbeType(SKOSBuilder):
    """Type of heat-flow probe used for measurement."""

    corer = Concept(
        {
            SKOS.prefLabel: _("Corer-outrigger"),
        }
    )

    bullard = Concept(
        {
            SKOS.prefLabel: _("Bullard probe"),
        }
    )

    violin_bow = Concept(
        {
            SKOS.prefLabel: _("Lister Violin-Bow probe"),
        }
    )

    ewing = Concept(
        {
            SKOS.prefLabel: _("Ewing probe"),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other probe"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Heat flow probe types"),
                SKOS.definition: _(
                    "Types of heat-flow probes used for collecting heat flow data, typically in marine settings."
                ),
            }
        )


class TransferMechanism(SKOSBuilder):
    """Specification of the predominant heat transfer mechanism relevant for the reported heatflow value."""

    conductive = Concept(
        {
            SKOS.prefLabel: _("Conductive"),
        }
    )

    convective = Concept(
        {
            SKOS.prefLabel: _("Convective unspecified"),
        }
    )

    upflow = Concept(
        {
            SKOS.prefLabel: _("Convective upflow"),
        }
    )

    downflow = Concept(
        {
            SKOS.prefLabel: _("Convective downflow"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Heat-flow specific transfer mechanisms"),
                SKOS.definition: _(
                    "Mechanisms of heat transfer though the Earth's crust."
                ),
            }
        )


class GeographicEnvironment(SKOSBuilder):
    """Specification of the geographic environment where the heat-flow measurement was performed."""

    onshore_continental = Concept(
        {
            SKOS.prefLabel: _("Onshore (continental)"),
        }
    )

    onshore_lake = Concept(
        {
            SKOS.prefLabel: _("Onshore (lake, river, etc.)"),
        }
    )

    offshore_continental = Concept(
        {
            SKOS.prefLabel: _("Offshore (continental)"),
        }
    )

    offshore_marine = Concept(
        {
            SKOS.prefLabel: _("Offshore (marine)"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Geographic environments"),
                SKOS.definition: _(
                    "Basic geographic environments where heat-flow measurements are performed."
                ),
            }
        )

        collections = {
            "onshore": Collection(
                {
                    SKOS.prefLabel: _("Onshore environments"),
                    SKOS.definition: _("Geographic environments found onshore."),
                    # SKOS.members:["onshore_continental", "onshore_lake"],
                }
            ),
            "offshore": Collection(
                {
                    SKOS.prefLabel: _("Offshore environments"),
                    SKOS.definition: _("Geographic environments found offshore."),
                    SKOS.member: ["offshore_continental", "offshore_marine"],
                }
            ),
        }


class ExplorationMethod(SKOSBuilder):
    """Specification of the general means by which the rock was accessed by temperature sensors for the respective data entry."""

    drilling = Concept(
        {
            SKOS.prefLabel: _("Drilling"),
        }
    )

    mining = Concept(
        {
            SKOS.prefLabel: _("Mining"),
        }
    )

    tunneling = Concept(
        {
            SKOS.prefLabel: _("Tunneling"),
        }
    )

    probing_onshore = Concept(
        {
            SKOS.prefLabel: _("Probing (onshore/lake, river, etc.)"),
        }
    )

    probing_offshore = Concept(
        {
            SKOS.prefLabel: _("Probing (offshore/ocean)"),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other (specify in comments)"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Exploration methods"),
                SKOS.definition: _(
                    "General means by which the rock was accessed by temperature sensors."
                ),
            }
        )


class ExplorationPurpose(SKOSBuilder):
    """Main purpose of the original excavation providing access for the temperature sensors."""

    hydrocarbon = Concept(
        {
            SKOS.prefLabel: _("Hydrocarbon"),
        }
    )

    underground_storage = Concept(
        {
            SKOS.prefLabel: _("Underground storage"),
        }
    )

    geothermal = Concept(
        {
            SKOS.prefLabel: _("Geothermal"),
        }
    )

    groundwater = Concept(
        {
            SKOS.prefLabel: _("Groundwater"),
        }
    )

    mapping = Concept(
        {
            SKOS.prefLabel: _("Mapping"),
        }
    )

    mining = Concept(
        {
            SKOS.prefLabel: _("Mining"),
        }
    )

    research = Concept(
        {
            SKOS.prefLabel: _("Research"),
        }
    )

    tunneling = Concept(
        {
            SKOS.prefLabel: _("Tunneling"),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other (specify in comments)"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Exploration purposes"),
                SKOS.definition: _(
                    "Main purpose of the original excavation providing access for the temperature sensors."
                ),
            }
        )


class TemperatureMethod(SKOSBuilder):
    """
    The allowed temperature methods for the T_method_top and T_method_bottom fields at the heat flow child level.


    **Continuous temperature logging** (using semiconductor transducer, or thermistor probe):

    * *LOGeq* - borehole in equilibrium
    * *LOGpert* - borehole perturbed
    * *cLOG* - perturbed but corrected

    **Distributed Temperature Sensing**:

    * *DTSeq* - in equilibrium
    * *DTSpert* - perturbed
    * *cDTS* - perturbed but corrected

    **Bottom Hole Temperature**:

    * *BHT* - uncorrected
    * *cBHT* - corrected

    **Drill stem test**:

    * *DST* - uncorrected
    * *cDST* - corrected for effects

    **Resistance temperature detectors**:

    * *RTDeq* - in equilibrium
    * *RTDpert* - perturbed
    * *cRTD* - perturbed but corrected

    **Ocean Drilling Temperature Tool**:

    * *ODTT-PC* - piston corer
    * *ODTT-TP* - thermistor probe

    **Other**:

    * *CPD* - Curie Point/Depth estimates
    * *XEN* - Xenolith
    * *GTM* - Geothermometry
    * *BSR* - bottom-simulating seismic reflector
    * *SUR* - surface temperature/bottom water temperature
    * *OTH* - other (method must be specified in comments)
    """

    LOGeq = Concept(
        {
            SKOS.prefLabel: _("LOGeq: borehole in equilibrium"),
        }
    )
    LOGpert = Concept(
        {
            SKOS.prefLabel: _("LOGpert: borehole perturbed"),
        }
    )
    cLOG = Concept(
        {
            SKOS.prefLabel: _("cLOG: perturbed but corrected"),
        }
    )
    DTSeq = Concept(
        {
            SKOS.prefLabel: _("DTSeq: in equilibrium"),
        }
    )
    DTSpert = Concept(
        {
            SKOS.prefLabel: _("DTSpert: perturbed"),
        }
    )
    cDTS = Concept(
        {
            SKOS.prefLabel: _("cDTS: perturbed but corrected"),
        }
    )
    BHT = Concept(
        {
            SKOS.prefLabel: _("BHT: uncorrected"),
        }
    )
    cBHT = Concept(
        {
            SKOS.prefLabel: _("cBHT: corrected"),
        }
    )
    DST = Concept(
        {
            SKOS.prefLabel: _("DST: uncorrected"),
        }
    )
    cDST = Concept(
        {
            SKOS.prefLabel: _("cDST: corrected"),
        }
    )
    RTDeq = Concept(
        {
            SKOS.prefLabel: _("RTDeq: in equilibrium"),
        }
    )
    RTDpert = Concept(
        {
            SKOS.prefLabel: _("RTDpert: perturbed"),
        }
    )
    cRTD = Concept(
        {
            SKOS.prefLabel: _("cRTD: perturbed but corrected"),
        }
    )
    ODTT_PC = Concept(
        {
            SKOS.prefLabel: _("ODTT-PC: piston corer"),
        }
    )
    ODTT_TP = Concept(
        {
            SKOS.prefLabel: _("ODTT-TP: thermistor probe"),
        }
    )
    CPD = Concept(
        {
            SKOS.prefLabel: _("CPD: Curie Point/Depth estimates"),
        }
    )
    XEN = Concept(
        {
            SKOS.prefLabel: _("XEN: Xenolith"),
        }
    )
    GTM = Concept(
        {
            SKOS.prefLabel: _("GTM: Geothermometry"),
        }
    )
    BSR = Concept(
        {
            SKOS.prefLabel: _("BSR: bottom-simulating seismic reflector"),
        }
    )
    SUR = Concept(
        {
            SKOS.prefLabel: _("SUR: surface temperature/bottom water temperature"),
        }
    )
    OTH = Concept(
        {
            SKOS.prefLabel: _("Other (method must be specified in comments)"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Temperature determination method"),
                SKOS.definition: _(
                    "Methods used to determine temperature for the purpose of deriving heat flow."
                ),
            }
        )


class TemperatureCorrection(SKOSBuilder):
    """Specification of the method used to correct the temperature data."""

    hornerPlot = Concept(
        {
            SKOS.prefLabel: _("Horner plot"),
        }
    )

    cylinderSource = Concept(
        {
            SKOS.prefLabel: _("Cylinder source method"),
        }
    )

    lineSourceExplosion = Concept(
        {
            SKOS.prefLabel: _("Line source explosion method"),
        }
    )

    inverseNM = Concept(
        {
            SKOS.prefLabel: _("Inverse numerical modelling"),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other published correction"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    not_corrected = Concept(
        {
            SKOS.prefLabel: _("not corrected"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Temperature correction methods"),
                SKOS.definition: _(
                    "Methods used to correct temperature data for the purpose of heat flow measurements."
                ),
            }
        )


class ConductivitySource(SKOSBuilder):
    """Specification of the source of the thermal conductivity data."""

    insitu_probe = Concept(
        {
            SKOS.prefLabel: _("In-situ probe"),
        }
    )

    core_log = Concept(
        {
            SKOS.prefLabel: _("Core-log integration"),
        }
    )

    core_samples = Concept(
        {
            SKOS.prefLabel: _("Core samples"),
        }
    )

    cutting_samples = Concept(
        {
            SKOS.prefLabel: _("Cutting samples"),
        }
    )

    outcrop_samples = Concept(
        {
            SKOS.prefLabel: _("Outcrop samples"),
        }
    )

    well_log = Concept(
        {
            SKOS.prefLabel: _("Well-log interpretation"),
        }
    )

    mineral_computation = Concept(
        {
            SKOS.prefLabel: _("Mineral computation"),
        }
    )

    assumed_from_literature = Concept(
        {
            SKOS.prefLabel: _("Assumed from literature"),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other (specify)"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Conductivity sources"),
            }
        )

        # collections = {
        #     "laboratory": Collection(
        #         SKOS.prefLabel:_("Laboratory"),
        #         SKOS.definition:_("Laboratory measurements"),
        #         SKOS.member:[
        #             "core_log",
        #             "core_samples",
        #             "cutting_samples",
        #             "outcrop_samples",
        #         ],
        #     ),
        #     "in_situ": Collection(
        #         SKOS.prefLabel:_("In-situ"),
        #         SKOS.definition:_("In-situ measurements"),
        #         SKOS.member:[
        #             "insitu_probe",
        #             "well_log",
        #         ],
        #     ),
        #     "computation": Collection(
        #         SKOS.prefLabel:_("Computation"),
        #         SKOS.definition:_("Computed values"),
        #         SKOS.member:[
        #             "mineral_computation",
        #             "assumed_from_literature",
        #         ],
        #     ),
        # }


class ConductivityMethod(SKOSBuilder):
    """Specification of the method used to determine the thermal conductivity."""

    pointSource = Concept(
        {
            SKOS.prefLabel: _("Lab - point source"),
        }
    )

    lineSourceFull = Concept(
        {
            SKOS.prefLabel: _("Lab - line source / full space"),
        }
    )

    lineSourceHalf = Concept(
        {
            SKOS.prefLabel: _("Lab - line source / half space"),
        }
    )

    planeSourceFull = Concept(
        {
            SKOS.prefLabel: _("Lab - plane source / full space"),
        }
    )

    planeSourceHalf = Concept(
        {
            SKOS.prefLabel: _("Lab - plane source / half space"),
        }
    )

    laboratoryOther = Concept(
        {
            SKOS.prefLabel: _("Lab - other"),
        }
    )

    probePulse = Concept(
        {
            SKOS.prefLabel: _("Probe - pulse technique"),
        }
    )

    wellLogDeterministic = Concept(
        {
            SKOS.prefLabel: _("Well-log - deterministic approach"),
        }
    )

    wellLogEmpirical = Concept(
        {
            SKOS.prefLabel: _("Well-log - empirical equation"),
        }
    )

    chlorineContent = Concept(
        {
            SKOS.prefLabel: _("Estimation - from chlorine content"),
        }
    )

    waterContent = Concept(
        {
            SKOS.prefLabel: _("Estimation - from water content/porosity"),
        }
    )

    lithology = Concept(
        {
            SKOS.prefLabel: _("Estimation - from lithology and literature"),
        }
    )

    mineralComposition = Concept(
        {
            SKOS.prefLabel: _("Estimation - from mineral composition"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Conductivity methods"),
                SKOS.definition: _(
                    "Methods used to calculate thermal conductivity in rock specimens or sections for the purpose of heat flow measurements."
                ),
            }
        )
        # collections = {
        #     "laboratory": Collection(
        #         SKOS.prefLabel:_("Laboratory"),
        #         SKOS.definition:_("Laboratory measurements"),
        #         SKOS.member:[
        #             "pointSource",
        #             "lineSourceFull",
        #             "lineSourceHalf",
        #             "planeSourceFull",
        #             "planeSourceHalf",
        #             "laboratoryOther",
        #         ],
        #     ),
        #     "probe": Collection(
        #         SKOS.prefLabel:_("Probe"),
        #         SKOS.definition:_("Probe measurements"),
        #         SKOS.member:[
        #             "probePulse",
        #         ],
        #     ),
        #     "well_log": Collection(
        #         SKOS.prefLabel:_("Well-log"),
        #         SKOS.definition:_("Well-log interpretation"),
        #         SKOS.member:[
        #             "wellLogDeterministic",
        #             "wellLogEmpirical",
        #         ],
        #     ),
        #     "estimation": Collection(
        #         SKOS.prefLabel:_("Estimation"),
        #         SKOS.definition:_("Estimation from other sources"),
        #         SKOS.member:[
        #             "chlorineContent",
        #             "waterContent",
        #             "lithology",
        #             "mineralComposition",
        #         ],
        #     ),
        #     "other": Collection(
        #         SKOS.prefLabel:_("Other"),
        #         SKOS.definition:_("Other methods"),
        #         SKOS.member:[
        #             "unspecified",
        #         ],
        #     ),
        # }


class ConductivityLocation(SKOSBuilder):
    """Specification of the location where the thermal conductivity was measured."""

    actual = Concept(
        {
            SKOS.prefLabel: _("Actual heat-flow location"),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other location"),
        }
    )

    literature = Concept(
        {
            SKOS.prefLabel: _("Literature/unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Conductivity location"),
            }
        )


class ConductivitySaturation(SKOSBuilder):
    """
    Specification of the saturation state of the rocks during the thermal conductivity measurement.
    """

    saturatedInSitu = Concept(
        {
            SKOS.prefLabel: _("Saturated measured in-situ"),
            SKOS.definition: _(
                "Insitu saturated measured (measurements with probe sensing / marine measurements)"
            ),
        }
    )

    recovered = Concept(
        {
            SKOS.prefLabel: _("Recovered"),
            SKOS.definition: _(
                "As recovered (rocks have been preserved and measured in close to their natural saturation state)."
            ),
        }
    )

    saturatedMeasured = Concept(
        {
            SKOS.prefLabel: _("Saturated measured"),
            SKOS.definition: _(
                "Saturated measured (rocks have been technically saturated completely before measurement)."
            ),
        }
    )

    saturatedCalculated = Concept(
        {
            SKOS.prefLabel: _("Saturated calculated"),
            SKOS.definition: _(
                "Thermal conductivity has been calculated from dry measured rocks, porosity and pore-filling fluid"
            ),
        }
    )

    dryMeasured = Concept(
        {
            SKOS.prefLabel: _("Dry measured"),
            SKOS.definition: _("Rocks have been technically dried before measurement"),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other"),
            SKOS.definition: _(
                "Other saturation state (must be specified in comments)"
            ),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Conductivity saturation state"),
            }
        )


class ConductivityPTConditions(SKOSBuilder):
    """
    Specification of the conditions under which the thermal conductivity was measured.
    """

    unrecordedAmbient = Concept(
        {
            SKOS.prefLabel: _("Unrecorded ambient pT conditions"),
        }
    )

    recordedAmbient = Concept(
        {
            SKOS.prefLabel: _("Recorded ambient pT conditions"),
        }
    )

    actualInSitu = Concept(
        {
            SKOS.prefLabel: _("Actual in-situ (pT) conditions"),
        }
    )

    replicatedP = Concept(
        {
            SKOS.prefLabel: _("Replicated in-situ (p)"),
        }
    )

    replicatedT = Concept(
        {
            SKOS.prefLabel: _("Replicated in-situ (T)"),
        }
    )

    replicatedPT = Concept(
        {
            SKOS.prefLabel: _("Replicated in-situ (pT)"),
        }
    )

    correctedP = Concept(
        {
            SKOS.prefLabel: _("Corrected in-situ (p)"),
        }
    )

    correctedT = Concept(
        {
            SKOS.prefLabel: _("Corrected in-situ (T)"),
        }
    )

    correctedPT = Concept(
        {
            SKOS.prefLabel: _("Corrected in-situ (pT)"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        name = "conductivity-pt-conditions"
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Conductivity measurement conditions"),
                SKOS.definition: _(
                    "Conditions under which the thermal conductivity was measured."
                ),
            }
        )

        # collections = {
        #     "recorded": Collection(
        #         SKOS.prefLabel:_("Recorded"),
        #         SKOS.definition:_(
        #             "Determinations under true conditions at target depths (e.g. sensing in boreholes)"
        #         ),
        #         SKOS.member:[
        #             "recordedAmbient",
        #         ],
        #     ),
        #     "replicated": Collection(
        #         SKOS.prefLabel:_("Replicated conditions"),
        #         SKOS.definition:_(
        #             "Determinations where the conditions at target depths are replicated under laboratory conditions"
        #         ),
        #         SKOS.member:[
        #             "replicatedP",
        #             "replicatedT",
        #             "replicatedPT",
        #         ],
        #     ),
        #     "corrected": Collection(
        #         SKOS.prefLabel:_("Corrected conditions"),
        #         SKOS.definition:_(
        #             "Determinations under laboratory pT conditions that were corrected to conditions at target depths"
        #         ),
        #         SKOS.member:[
        #             "correctedP",
        #             "correctedT",
        #             "correctedPT",
        #         ],
        #     ),
        #     "actual": Collection(
        #         SKOS.prefLabel:_("Actual"),
        #         SKOS.definition:_(
        #             "The condition at the respective depth of the heat-flow interval."
        #         ),
        #         SKOS.member:[
        #             "actualInSitu",
        #         ],
        #     ),
        # }


class ConductivityStrategy(SKOSBuilder):
    """
    Specification of the strategy used to determine the thermal conductivity.
    """

    random = Concept(
        {
            SKOS.prefLabel: _("Random or periodic depth sampling (number)"),
            SKOS.definition: _("Random or periodic depth sampling (number)"),
        }
    )

    characterize = Concept(
        {
            SKOS.prefLabel: _("Characterize formation conductivities"),
            SKOS.definition: _("Characterize formation conductivities"),
        }
    )

    well_log = Concept(
        {
            SKOS.prefLabel: _("Well log interpretation"),
            SKOS.definition: _("Well log interpretation"),
        }
    )

    computation = Concept(
        {
            SKOS.prefLabel: _("Computation from probe sensing"),
            SKOS.definition: _("Computation from probe sensing"),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other"),
            SKOS.definition: _("Other"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
            SKOS.definition: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Thermal conductivity strategy"),
                SKOS.definition: _(
                    "Strategy by which thermal conductivity for a particular heat flow interval was calculated."
                ),
            }
        )


class ConductivityPTFunction(SKOSBuilder):
    """
    Specification of the function used to determine the thermal conductivity.
    """

    Tikhomirov1968 = Concept(
        {
            SKOS.prefLabel: "T - Tikhomirov (1968)",
        }
    )

    KutasGordienko1971 = Concept(
        {
            SKOS.prefLabel: "Kutas & Gordienko (1971)",
        }
    )

    Anand1973 = Concept(
        {
            SKOS.prefLabel: "Anand et al. (1973)",
        }
    )

    HaenelZoth1973 = Concept(
        {
            SKOS.prefLabel: "Haenel & Zoth (1973)",
        }
    )

    Blesch1983 = Concept(
        {
            SKOS.prefLabel: "Blesch et al. (1983)",
        }
    )

    Sekiguchi1984 = Concept(
        {
            SKOS.prefLabel: "Sekiguchi (1984)",
        }
    )

    Chapman1984 = Concept(
        {
            SKOS.prefLabel: "Chapman et al. (1984)",
        }
    )

    ZothHaenal1988 = Concept(
        {
            SKOS.prefLabel: "Zoth & Haenel (1988)",
        }
    )

    Somerton1992 = Concept(
        {
            SKOS.prefLabel: "Somerton (1992)",
        }
    )

    Sass1992 = Concept(
        {
            SKOS.prefLabel: "Sass et al. (1992)",
        }
    )

    Funnell1996 = Concept(
        {
            SKOS.prefLabel: "Funnell et al. (1996)",
        }
    )

    Kukkonen1999 = Concept(
        {
            SKOS.prefLabel: "Kukkonen et al. (1999)",
        }
    )

    Seipold2001 = Concept(
        {
            SKOS.prefLabel: "Seipold (2001)",
        }
    )

    VosteenSchellschmidt2003 = Concept(
        {
            SKOS.prefLabel: "Vosteen & Schellschmidt (2003)",
        }
    )

    Sun2017 = Concept(
        {
            SKOS.prefLabel: "Sun et al. (2017)",
        }
    )

    Miranda2018 = Concept(
        {
            SKOS.prefLabel: "Miranda et al. (2018)",
        }
    )

    Ratcliff1960 = Concept(
        {
            SKOS.prefLabel: "Ratcliff (1960)",
        }
    )

    Bridgman1924 = Concept(
        {
            SKOS.prefLabel: "Bridgman (1924)",
        }
    )

    Sibbitt1975 = Concept(
        {
            SKOS.prefLabel: "Sibbitt (1975)",
        }
    )

    Kukkonen1999 = Concept(
        {
            SKOS.prefLabel: "Kukkonen et al. (1999)",
        }
    )

    Seipold2001 = Concept(
        {
            SKOS.prefLabel: "Seipold (2001)",
        }
    )

    Duruturk2002 = Concept(
        {
            SKOS.prefLabel: "Durutürk et al. (2002)",
        }
    )

    Demirci2004 = Concept(
        {
            SKOS.prefLabel: "Demirci et al. (2004)",
        }
    )

    Gorgulu2008 = Concept(
        {
            SKOS.prefLabel: "Görgülü et al. (2008)",
        }
    )

    FuchsFoerster2014 = Concept(
        {
            SKOS.prefLabel: "Fuchs & Förster (2014)",
        }
    )

    Radcliff1960 = Concept(
        {
            SKOS.prefLabel: "Radcliff (1960)",
        }
    )

    Buntebarth1991 = Concept(
        {
            SKOS.prefLabel: "Buntebarth (1991)",
        }
    )

    ChapmanFurlong1992 = Concept(
        {
            SKOS.prefLabel: "Chapman & Furlong (1992)",
        }
    )

    Emirov1997 = Concept(
        {
            SKOS.prefLabel: "Emirov et al. (1997)",
        }
    )

    Abdulagatov2006 = Concept(
        {
            SKOS.prefLabel: "Abdulagatov et al. (2006)",
        }
    )

    EmirovRamazanova2007 = Concept(
        {
            SKOS.prefLabel: "Emirov & Ramazanova (2007)",
        }
    )

    Abdulagatova2009 = Concept(
        {
            SKOS.prefLabel: "Abdulagatova et al. (2009)",
        }
    )

    RamazanovaEmirov2010 = Concept(
        {
            SKOS.prefLabel: "Ramazanova & Emirov (2010)",
        }
    )

    RamazanovaEmirov2012 = Concept(
        {
            SKOS.prefLabel: "Ramazanova & Emirov (2012)",
        }
    )

    Emirov2017 = Concept(
        {
            SKOS.prefLabel: "Emirov et al. (2017)",
        }
    )

    site_specific = Concept(
        {
            SKOS.prefLabel: _("Site-specific experimental relationships"),
        }
    )

    other = Concept(
        {
            SKOS.prefLabel: _("Other"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        name = "conductivity-pt-function"
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Conductivity PT function"),
            }
        )
        # collections = {
        #     "temperature": Collection(
        #         SKOS.prefLabel:_("Temperature"),
        # }
        #         SKOS.member:[
        #             "Tikhomirov1968",
        #             "KutasGordienko1971",
        #             "Anand1973",
        #             "HaenelZoth1973",
        #             "Blesch1983",
        #             "Sekiguchi1984",
        #             "Chapman1984",
        #             "ZothHaenal1988",
        #             "Somerton1992",
        #             "Sass1992",
        #             "Funnell1996",
        #             "Kukkonen1999",
        #             "Seipold2001",
        #             "VosteenSchellschmidt2003",
        #             "Sun2017",
        #             "Miranda2018",
        #             "Ratcliff1960",
        #         ],
        #     ),
        #     "pressure": Collection(
        #         SKOS.prefLabel:_("Pressure"),
        # }
        #         SKOS.member:[
        #             "Bridgman1924",
        #             "Sibbitt1975",
        #             "Kukkonen1999",
        #             "Seipold2001",
        #             "Duruturk2002",
        #             "Demirci2004",
        #             "Gorgulu2008",
        #             "FuchsFoerster2014",
        #         ],
        #     ),
        #     "pressure_temperature": Collection(
        #         SKOS.prefLabel:_("Pressure and Temperature"),
        # }
        #         SKOS.member:[
        #             "Radcliff1960",
        #             "Buntebarth1991",
        #             "ChapmanFurlong1992",
        #             "Emirov1997",
        #             "Abdulagatov2006",
        #             "EmirovRamazanova2007",
        #             "Abdulagatova2009",
        #             "RamazanovaEmirov2010",
        #             "RamazanovaEmirov2012",
        #             "Emirov2017",
        #         ],
        #     ),
        # }


class GenericFlagChoices(SKOSBuilder):
    """Generic flag choices for heat flow data."""

    present_corrected = Concept(
        {
            SKOS.prefLabel: _("Present and corrected"),
        }
    )

    present_not_corrected = Concept(
        {
            SKOS.prefLabel: _("Present and not corrected"),
        }
    )

    present_not_significant = Concept(
        {
            SKOS.prefLabel: _("Present not significant"),
        }
    )

    not_recognized = Concept(
        {
            SKOS.prefLabel: _("not recognized"),
        }
    )

    consideredP = Concept(
        {
            SKOS.prefLabel: _("Considered - pressure"),
        }
    )

    consideredT = Concept(
        {
            SKOS.prefLabel: _("Considered - temperature"),
        }
    )

    consideredPT = Concept(
        {
            SKOS.prefLabel: _("Considered - pT"),
        }
    )

    notConsidered = Concept(
        {
            SKOS.prefLabel: _("Not considered"),
        }
    )

    tiltCorrected = Concept(
        {
            SKOS.prefLabel: _("Tilt corrected"),
        }
    )

    driftCorrected = Concept(
        {
            SKOS.prefLabel: _("Drift corrected"),
        }
    )

    notCorrected = Concept(
        {
            SKOS.prefLabel: _("Not corrected"),
        }
    )

    corrected = Concept(
        {
            SKOS.prefLabel: _("Corrected (specify)"),
        }
    )

    unspecified = Concept(
        {
            SKOS.prefLabel: _("Unspecified"),
        }
    )

    class Meta(BaseMeta):
        namespace_separator = "#"
        prefix = BASE_PREFIX
        base_url = BASE_URL
        name = "correction-flags"
        scheme = ConceptScheme(
            {
                SKOS.prefLabel: _("Generic flag choices"),
            }
        )
        # collections = {
        #     "generic": Collection(
        #         SKOS.prefLabel:_("Generic"),
        #         SKOS.definition:_("Generic flag choices for heat flow data"),
        #         SKOS.member:[
        #             "present_corrected",
        #             "present_not_corrected",
        #             "present_not_significant",
        #             "unrecognized",
        #             "unspecified",
        #         ],
        #     ),
        #     "insitu": Collection(
        #         SKOS.prefLabel:_("In-situ"),
        #         SKOS.definition:_("In-situ measurements"),
        #         SKOS.member:[
        #             "consideredP",
        #             "consideredT",
        #             "consideredPT",
        #             "notConsidered",
        #             "unspecified",
        #         ],
        #     ),
        #     "temperature": Collection(
        #         SKOS.prefLabel:_("Temperature"),
        #         SKOS.definition:_("Temperature measurements"),
        #         SKOS.member:[
        #             "tiltCorrected",
        #             "driftCorrected",
        #             "notCorrected",
        #             "corrected",
        #             "unspecified",
        #         ],
        #     ),
        # }


# q = HeatFlowMethod()
# print(q.serialize(format="turtle"))

# test = 9
