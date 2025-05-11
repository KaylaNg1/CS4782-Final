import torch
import torch.nn.functional as F

def optimize_noise(generator, w_plus, target_image, 
                   num_steps=3000, 
                   lr=0.01, 
                   normalize_every=100, 
                   perceptual_loss_fn=None, 
                   perceptual_weight=0.1):
    """
    Optimize the noise maps of StyleGAN generator to improve fine detail reconstruction.

    Args:
        generator (torch.nn.Module): The StyleGAN generator model.
        w_plus (torch.Tensor): Latent code (W+ space) with shape (batch_size, 18, 512).
        target_image (torch.Tensor): The target image tensor (batch_size, 3, H, W).
        num_steps (int): Number of optimization steps for noise.
        lr (float): Learning rate for noise optimization.
        normalize_every (int): Frequency (in steps) to normalize noise maps.
        perceptual_loss_fn (callable, optional): VGG-based perceptual loss function. 
        perceptual_weight (float): Weight for perceptual loss if used.
        
    Returns:
        optimized_noise (list of torch.Tensor): List of optimized noise maps.
    """
    # 1. Extract NoiseLayer weights
    noise_maps = []
    for module in generator.modules():
        if isinstance(module, NoiseLayer):
            noise_maps.append(module.weight)

    # 2. Clone and make trainable
    noise_maps = [n.clone().detach().requires_grad_(True) for n in noise_maps]

    # 3. Setup optimizer
    noise_optimizer = torch.optim.Adam(noise_maps, lr=lr)

    # 4. Optimization loop
    for step in range(num_steps):
        noise_optimizer.zero_grad()

        # Re-generate image using fixed W+ and current noise maps
        # Important: set the generator's noise layers to current trainable noise maps
        idx = 0
        for module in generator.modules():
            if isinstance(module, NoiseLayer):
                module.weight = noise_maps[idx]
                idx += 1

        generated_image = generator(w_plus)

        # Compute pixel loss
        pixel_loss = F.mse_loss(generated_image, target_image)

        # Optionally, add perceptual loss
        loss = pixel_loss
        if perceptual_loss_fn is not None:
            perceptual_loss = perceptual_loss_fn(generated_image, target_image)
            loss += perceptual_weight * perceptual_loss

        loss.backward()
        noise_optimizer.step()

        # Normalize noise maps periodically
        if (step + 1) % normalize_every == 0:
            with torch.no_grad():
                for n in noise_maps:
                    n -= n.mean()
                    n /= (n.std() + 1e-8)

        if step % 500 == 0 or step == num_steps - 1:
            print(f"[Noise Step {step+1}/{num_steps}] Loss: {loss.item():.6f}")

    return noise_maps
