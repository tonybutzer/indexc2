import datacube

from datacube.index.hl import Doc2Dataset


def add_dataset(doc, uri, index, sources_policy):
    logging.info("Indexing %s", uri)
    resolver = Doc2Dataset(index)
    dataset, err = resolver(doc, uri)
    if err is not None:
        logging.error("%s", err)
    else:
        try:
            index.datasets.add(dataset,
                               sources_policy=sources_policy)  # Source policy to be checked in sentinel 2 datase types
        except changes.DocumentMismatchError as e:
            index.datasets.update(dataset, {tuple(): changes.allow_any})
        except Exception as e:
            err = e
            logging.error("Unhandled exception %s", e)

    return dataset, err
