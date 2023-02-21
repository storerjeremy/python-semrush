# pyrush

Pyrush is a wrapper around the [`SEMrush API`](http://www.semrush.com/api-documentation/) version 3.0.

Forked from: https://github.com/storerjeremy/python-semrush

Thanks to [`storerjeremy`](https://github.com/storerjeremy) and [`tomlintin`](https://github.com/tomlinton) for the basis of this package.

# Installation

You can install pyrush from github.

    $ pip install git+https://github.com/charliemday/pyrush.git

# Usage

    from pyrush.semrush import SemrushClient
    client = SemrushClient(key='your_semrush_api_key')
    result = client.domain_ranks(domain='example.com')

# Todo

- Implement projects API http://www.semrush.com/api-projects/
- Implement accounts API http://www.semrush.com/api-accounts/
- Implement specific errors

# License

This software is licensed under the `MIT License`. See the `LICENSE`
file in the top distribution directory for the full license text.
