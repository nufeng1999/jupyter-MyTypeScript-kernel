from ipykernel.kernelapp import IPKernelApp
from .kernel import MyTypeScriptKernel
IPKernelApp.launch_instance(kernel_class=MyTypeScriptKernel)
