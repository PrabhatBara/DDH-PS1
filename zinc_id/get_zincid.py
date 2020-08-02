import sys


# Load Python version specific modules
if sys.version_info[0] == 3:
    import urllib.request
    import urllib.parse
else:
    import urllib




def get_zincid_from_smile(smile_str, backend='zinc15'):
    """
    Gets the corresponding ZINC ID(s) for a SMILE string query from
    the ZINC online database. Requires an internet connection.
    Keyword arguments:
        smile_str (str): A valid SMILE string, e.g.,
            C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O'
        backend (str): Specifies the database backend, "zinc12" or "zinc15"
    Returns the SMILE string for the corresponding ZINC ID(s) in a list.
        E.g., ['ZINC01234567', 'ZINC01234568', 'ZINC01242053', 'ZINC01242055']
    """

    if backend not in {'zinc12', 'zinc15'}:
        raise ValueError("backend must be 'zinc12' or 'zinc15'")

    stripped_smile = smile_str.strip()
    encoded_smile = urllib.parse.quote(stripped_smile)

    if backend == 'zinc12':
        url_part1 = 'http://zinc12.docking.org/results?structure.smiles='
        url_part3 = '&structure.similarity=1.0'
    elif backend == 'zinc15':
        url_part1 = 'http://zinc.docking.org/substances/search/?q='
        url_part3 = ''
    else:
        raise ValueError("Backend must be 'zinc12' or 'zinc15'. "
                         "Got %s" % (backend))

    zinc_ids = []

    try:
        if sys.version_info[0] == 3:
            #smile_url = urllib.request.pathname2url(encoded_smile)
            response = urllib.request.urlopen('{}{}{}'
                                              .format(url_part1,
                                                      encoded_smile,
                                                      url_part3))
        else:
            #smile_url = urllib.pathname2url(encoded_smile)
            response = urllib.urlopen('{}{}{}'
                                      .format(url_part1,
                                              encoded_smile,
                                              url_part3))
    except urllib.error.HTTPError:
        print('Invalid SMILE string {}'.format(smile_str))
        response = []
    for line in response:
        line = line.decode(encoding='UTF-8').strip()

        if backend == 'zinc15':
            if line.startswith('<a href="/substances/ZINC'):
                line = line.split('/')[-2]
                if sys.version_info[0] == 3:
                    zinc_id = urllib.parse.unquote(line)
                else:
                    zinc_id = urllib.unquote(line)
                zinc_ids.append(str(zinc_id))
        else:
            if line.startswith('<a href="//zinc.docking.org/substance/'):
                line = line.split('</a>')[-2].split('>')[-1]
                if sys.version_info[0] == 3:
                    zinc_id = urllib.parse.unquote(line)
                else:
                    zinc_id = urllib.unquote(line)
                zinc_id = 'ZINC' + (8-len(zinc_id)) * '0' + zinc_id
                zinc_ids.append(str(zinc_id))
    return zinc_ids