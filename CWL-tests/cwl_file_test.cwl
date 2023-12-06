cwlVersion: v1.2
class: CommandLineTool
baseCommand: ['/bin/bash', 'stageout.sh']
hints:
  DockerRequirement:
    dockerPull: terradue/stars:2.3.1
inputs:
  example_file:
    type: string?
    inputBinding:
      position: 1

outputs: []
