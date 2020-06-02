# Typeshed in Medi

Typeshed is used in Medi to provide completions for all the stdlib modules.

The relevant files in medi are in `medi/inference/gradual`. `gradual` stands
for "gradual typing".

## Updating Typeshed

Currently Medi has a custom implementation hosted in
https://github.com/davidhalter/typeshed.git for two reasons:

- Medi doesn't understand Tuple.__init__ properly.
- Typeshed has a bug: https://github.com/python/typeshed/issues/2999

Therefore we need a bit of a complicated process to upgrade typeshed:

    cd medi/third_party/typeshed
    git remote add upstream https://github.com/python/typeshed
    git fetch upstream
    git checkout medi
    git rebase upstream/master
    git push -f

    git push
    cd ../../..
    git commit medi/third_party/typeshed -m "Upgrade typeshed"

If merge conflicts appear, just make sure that only one commit from Medi
appears.
