"""This module is intended to handle versioning the documentation."""

import pathlib
import semver


def get_conf_lines():
    """Open the conf.py file and return the contents as a list."""
    cur_fp = pathlib.Path(__file__).parent
    with pathlib.Path(f"{cur_fp}/conf.py").open("r", encoding="utf-8") as cf_fh:
        c_lines = cf_fh.readlines()
    return c_lines


def get_release_index(c_lines: list):
    """Iterate the list of lines to find the release."""
    ret_value = 0
    for index, line_str in enumerate(c_lines):
        if "release = " in line_str:
            ret_value = index
    return ret_value


def parse_version_string(c_lines: list, index: int):
    """Get the version number for semver."""
    ver_str = c_lines[index].replace("release = ", "").replace("'", "")
    ver_semver = semver.parse_version_info(ver_str)
    return ver_semver


def increment_patch(ver_semver: semver.VersionInfo):
    """Increment the patch number."""
    return ver_semver.bump_patch()


def get_new_conf_lines(c_lines: list, index: int, new_release: semver.VersionInfo):
    """Set the new release line."""
    c_lines[index] = f"release = '{new_release}'"
    return c_lines


def write_new_version(c_lines: list):
    """Save the updated release version."""
    with pathlib.Path("../conf.py").open("w", encoding="utf-8") as c_fh:
        c_fh.writelines(c_lines)


if __name__ == "__main__":
    conf_lines = get_conf_lines()
    rindex = get_release_index(conf_lines)
    prev_ver = parse_version_string(conf_lines, rindex)
    new_ver = increment_patch(prev_ver)
    new_conf_lines = get_new_conf_lines(conf_lines, rindex, new_ver)
    print(new_conf_lines)
