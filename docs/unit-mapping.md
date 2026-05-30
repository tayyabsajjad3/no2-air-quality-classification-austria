# Unit Mapping (T2.3)

## Overview

This document maps every numeric attribute in the NO2 air quality dataset to an
ontological unit concept, addressing the **Interoperability** aspect of FAIR data.

### Primary Ontology: QUDT (Quantities, Units, Dimensions and Types)

The recommended primary ontology for this task is the **SI Digital Framework**
(https://si-digital-framework.org/). However, the SI Digital Framework defines only
the seven SI base units and their direct coherent derived units (e.g. kg·m⁻³). The
key measurement unit in this dataset — microgram per cubic metre (µg·m⁻³) — is a
**prefixed derived unit** not directly represented in the SI Digital Framework TTL
serialisation. Per the task instructions, the designated fall-back ontology is
**QUDT** (https://www.omg.org/spec/Commons/QuantitiesAndUnits.ttl), which provides
explicit URIs for prefixed units including `unit:MicroGM-PER-M3`. QUDT is a
well-established, actively maintained ontology widely used in environmental and
scientific data publishing, making it the appropriate choice here.

---

## Attribute Unit Mapping Table

| Attribute | Data Type | Physical Quantity | Unit Symbol | Unit Label | Ontology | Unit URI |
|-----------|-----------|------------------|-------------|------------|----------|----------|
| `Value` | float (object) | Mass concentration of NO₂ in air | µg·m⁻³ | Microgram Per Cubic Metre | QUDT | `http://qudt.org/vocab/unit/MicroGM-PER-M3` |
| `DataCapture` | float (object) | Data capture ratio (fraction of valid measurements in aggregation period) | 1 (dimensionless fraction) | Fraction | QUDT | `http://qudt.org/vocab/unit/FRACTION` |
| `Start` | datetime64[ns] | Start timestamp of measurement interval | s (ISO 8601 encoding) | Second | QUDT | `http://qudt.org/vocab/unit/SEC` |
| `End` | datetime64[ns] | End timestamp of measurement interval | s (ISO 8601 encoding) | Second | QUDT | `http://qudt.org/vocab/unit/SEC` |
| `ResultTime` | datetime64[ns] | Time at which the result was produced | s (ISO 8601 encoding) | Second | QUDT | `http://qudt.org/vocab/unit/SEC` |
| `Validity` | int32 | EEA validity flag (−1 = not validated, 0 = invalid, 1 = valid, 2 = valid corrected, 3 = preliminary) | — | Dimensionless integer code | — | No unit applicable (ordinal classification code) |
| `Verification` | int32 | EEA verification flag (0 = not verified, 1 = verified, 2 = inconclusive) | — | Dimensionless integer code | — | No unit applicable (ordinal classification code) |
| `Pollutant` | int32 | EEA internal pollutant identifier | — | Dimensionless integer identifier | — | No unit applicable (nominal identifier) |

---

## Quantity Kind Mapping

In addition to units, QUDT also defines *quantity kinds* (what physical property is
being measured). These are listed below for completeness:

| Attribute | Quantity Kind Label | Quantity Kind URI |
|-----------|--------------------|--------------------|
| `Value` | Mass Concentration | `http://qudt.org/vocab/quantitykind/MassConcentration` |
| `DataCapture` | Dimensionless Ratio | `http://qudt.org/vocab/quantitykind/DimensionlessRatio` |
| `Start` / `End` / `ResultTime` | Time | `http://qudt.org/vocab/quantitykind/Time` |

---

## Notes

- **`Value` column** is stored as `object` dtype in the raw Parquet files due to
  occasional null/sentinel values from the EEA source. When loaded into DBRepo, this
  column is treated as `DOUBLE PRECISION` / `FLOAT` with nullable values.
- **`DataCapture`** was `None` in the sampled station file (`SPO.09.A23.65511.8.1`),
  indicating missing data capture metadata for that station. The unit mapping still
  applies wherever values are present.
- **Temporal columns** (`Start`, `End`, `ResultTime`) represent absolute UTC
  timestamps encoded in ISO 8601 format. The QUDT second unit applies to the
  underlying time dimension; the actual storage format is `TIMESTAMP WITH TIME ZONE`.
- **`Validity` and `Verification`** are ordinal integer codes defined by the EEA
  reporting vocabulary. They carry no physical unit and are not mapped to a unit
  ontology concept. Their semantics are documented in the EEA Air Quality data
  specification.

---

## References

- QUDT Ontology: https://qudt.org/
- QUDT Unit `MicroGM-PER-M3`: http://qudt.org/vocab/unit/MicroGM-PER-M3
- QUDT Unit `FRACTION`: http://qudt.org/vocab/unit/FRACTION
- QUDT Unit `SEC`: http://qudt.org/vocab/unit/SEC
- SI Digital Framework: https://si-digital-framework.org/
- EEA Air Quality Data Hub: https://www.eea.europa.eu/en/datahub/datahubitem-view/778ef9f5-6293-4846-badd-56a29c70880d