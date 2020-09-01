Документ cat.cwl:

cwlVersion: v1.0
class: CommandLineTool

inputs:
  input_file:
    type: File
    inputBinding:
      position: 1

outputs:
  output_file:
    type: File
    outputBinding:
      glob: output.txt

baseCommand: cat
stdout: output.txt

 Входные параметры cat.yml:

input_file:
  class: File
  path: hello.txt

Два равнозначных варианта запуска:

cwltool cat.cwl cat.yml
cwltool cat.cwl --input_file hello.txt
