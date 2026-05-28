# CodeMeta Notes

`codemeta.json` has been drafted from the current repository metadata, the pinned dependencies in `requirements.txt`, and the current Zenodo DOI recorded in `CITATION.cff`.

Before final submission, the group must add each author's ORCID to the corresponding `Person` object. The assignment explicitly requires authors with ORCIDs, and these identifiers should not be guessed.

The dependency list should be regenerated after the final implementation is complete. If the project adds packages for DBRepo access, model training, FAIR4ML, RO-Crate validation, or Croissant metadata generation, those packages must be pinned in `requirements.txt` and reflected in `codemeta.json`.
