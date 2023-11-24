import syft as sy
import numpy as np

# Create a hook to extend PyTorch with PySyft functionality
hook = sy.TorchHook()

# Create a "virtual" machine to simulate a remote machine
bob = sy.VirtualWorker(hook, id="bob")

# Define data
data = np.array([1, 2, 3, 4, 5])
data = sy.Tensor(data).send(bob)

# Encrypt the data
encrypted_data = data.fix_prec().share(bob, crypto_provider=bob)

# Perform computations on the encrypted data
result = encrypted_data + encrypted_data

# Decrypt the result
decrypted_result = result.get().float_prec()

print("Encrypted result:", result)
print("Decrypted result:", decrypted_result)
