# Tmux System Info Status

Enables displaying system information in Tmux `status-right` and `status-left`.

## Installation

### Installation with [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)

Add plugin to the list of TPM plugins in `.tmux.conf`:

    set -g @plugin 'cctags/tmux-system-info'

Hit `prefix + I` to fetch the plugin and source it.

If format strings are added to `status-right`, they should now be visible.

### Manual Installation

``TODO``

### Optional requirement for Linux

+ python3
+ [psutil](https://pypi.org/project/psutil)

## Usage

Add any of the supported format strings (see below) to the existing `status-right` tmux option.
Example:

    # in .tmux.conf
    set -g status-right '#{system_info} | %a %h-%d %H:%M '

### Supported Options

This is done by introducing 8 new format strings that can be added to
`status-right` option:

 - `#{system_info}` - will display system info

### Acknowledgments

This code is originally based on the [tmux-cpu](https://github.com/tmux-plugins/tmux-cpu) project.

### License

[MIT](LICENSE)
