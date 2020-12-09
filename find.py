import semantic_version


""" Find closest lower semantic version value """
def find_closest_version(semver_string, semver_list):
    result = []
    if len(semver_list):
        v2 = semantic_version.Version(semver_string)
        sorted_semver_list = sorted(semver_list)
        if semver_string in semver_list:
            return semver_string
        else:
            for version in sorted_semver_list:
                v1 = semantic_version.Version(version)
                if v1 <= v2:
                    result.append(v1)
        return result[-1]
              
    else:
        return None


""" HOW USE """
versions = ['1.0.0', '2.0.0', '1.99.0', '2.2.2', '4.55.12', '1.5.0', '1.6.1', '6.0.0', '10.1.0']
version = '2.0.1'
print(find_closest_version(version, versions))
