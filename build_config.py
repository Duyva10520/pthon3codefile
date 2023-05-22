def build_vrf_config(vrf_name, rd, rt_import='', rt_export=''):
    rt_import = rd if not rt_import else rt_import
    rt_export = rd if not rt_export else rt_export
    
    return f"""
    vrf name {vrf_name}
    rd {rd}
    address-family ipv4
    route-target import {rt_import}
    route-target export {rt_export}
    """
