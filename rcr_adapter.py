from rcr import command_log_to_rcr_map
from model import BuildRCRMapRequest, BuildRCRMapResult


def command_log_to_rcr_adapter(rcr_map_request: BuildRCRMapRequest) -> BuildRCRMapResult:
    rcr_map = command_log_to_rcr_map(rcr_map_request.commands)
    return BuildRCRMapResult(rcr_map=rcr_map)
