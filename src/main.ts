import './style.css';
import { Chart, Flash, Lock, ArrowRight, Check } from 'iconoir';

// Types
interface LeadData {
  name: string;
  email: string;
  phone?: string;
  company?: string;
  message?: string;
}

interface SnaptrWindow extends Window {
  snaptr?: (action: string, event: string, data?: Record<string, unknown>) => void;
}

// Configuration
const WEBHOOK_URL = 'https://landing-bot-client-france-production.up.railway.app/webhook/lead';

// App state
let isSubmitting = false;

// Create icon wrapper
const createIcon = (IconComponent: string, size = 24): string => {
  return `<svg width="${size}" height="${size}" stroke-width="1.5" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">${IconComponent}</svg>`;
};

// Render Hero Section
const renderHero = (): string => {
  return `
    <section class="hero">
      <div class="hero-content">
        <div class="hero-text">
          <span class="hero-label">Nouveau</span>
          <h1>Transformez vos visiteurs en clients</h1>
          <p>La solution complète pour capturer, analyser et convertir vos leads avec une précision inégalée.</p>
          <a href="#form" class="cta-button">
            Commencer gratuitement
            <span class="icon">${ArrowRight}</span>
          </a>
        </div>
        <div class="form-card" id="form">
          <h2>Démarrez maintenant</h2>
          <p class="form-subtitle">Essai gratuit. Sans engagement.</p>
          <form id="leadForm">
            <div class="form-group">
              <label for="name">Nom complet</label>
              <input type="text" id="name" name="name" required placeholder="Jean Dupont" autocomplete="name">
            </div>
            <div class="form-group">
              <label for="email">Adresse e-mail</label>
              <input type="email" id="email" name="email" required placeholder="jean@entreprise.fr" autocomplete="email">
            </div>
            <div class="form-group">
              <label for="phone">Téléphone</label>
              <input type="tel" id="phone" name="phone" placeholder="+33 6 12 34 56 78" autocomplete="tel">
            </div>
            <div class="form-group">
              <label for="company">Entreprise</label>
              <input type="text" id="company" name="company" placeholder="Votre entreprise" autocomplete="organization">
            </div>
            <div class="form-group">
              <label for="message">Comment pouvons-nous vous aider ?</label>
              <textarea id="message" name="message" rows="3" placeholder="Décrivez votre projet..."></textarea>
            </div>
            <button type="submit" class="submit-button">
              <span class="button-text">Envoyer ma demande</span>
            </button>
          </form>
        </div>
      </div>
    </section>
  `;
};

// Render Features Section
const renderFeatures = (): string => {
  const features = [
    {
      icon: Chart,
      title: 'Analytics en temps réel',
      description: 'Suivez vos conversions minute par minute avec des données précises et actionnables.'
    },
    {
      icon: Flash,
      title: 'Performance extrême',
      description: 'Pages ultra-rapides optimisées pour le SEO et une expérience utilisateur exceptionnelle.'
    },
    {
      icon: Lock,
      title: 'Sécurité totale',
      description: 'Protection maximale de vos données avec conformité RGPD garantie.'
    }
  ];

  const featuresHTML = features.map(feature => `
    <div class="feature-card">
      <div class="feature-icon">${feature.icon}</div>
      <h3>${feature.title}</h3>
      <p>${feature.description}</p>
    </div>
  `).join('');

  return `
    <section class="features fade-in-section">
      <div class="features-container">
        <div class="section-label">Fonctionnalités</div>
        <h2 class="section-title">Pourquoi nous choisir ?</h2>
        <p class="section-subtitle">Des outils puissants pour maximiser vos conversions et développer votre business.</p>
        <div class="features-grid">
          ${featuresHTML}
        </div>
      </div>
    </section>
  `;
};

// Render Success Overlay
const renderSuccessOverlay = (): string => {
  return `
    <div id="successOverlay" class="success-overlay">
      <div class="success-message">
        <div class="success-icon">${Check}</div>
        <h2>Merci !</h2>
        <p>Votre demande a été envoyée avec succès. Notre équipe vous contactera très bientôt.</p>
      </div>
    </div>
  `;
};

// Handle form submission
const handleFormSubmit = async (e: Event): Promise<void> => {
  e.preventDefault();
  
  if (isSubmitting) return;
  isSubmitting = true;

  const form = e.target as HTMLFormElement;
  const submitButton = form.querySelector('.submit-button') as HTMLButtonElement;
  const buttonText = submitButton.querySelector('.button-text') as HTMLElement;

  // Loading state
  submitButton.disabled = true;
  buttonText.innerHTML = '<span class="spinner"></span>';

  // Get form data
  const formData: LeadData = {
    name: (form.querySelector('#name') as HTMLInputElement).value,
    email: (form.querySelector('#email') as HTMLInputElement).value,
    phone: (form.querySelector('#phone') as HTMLInputElement).value || 'Non renseigné',
    company: (form.querySelector('#company') as HTMLInputElement).value || 'Non renseigné',
    message: (form.querySelector('#message') as HTMLTextAreaElement).value || 'Aucun message'
  };

  // Snapchat tracking
  const snaptrWindow = window as SnaptrWindow;
  if (snaptrWindow.snaptr) {
    snaptrWindow.snaptr('track', 'SIGN_UP', {
      user_email: formData.email
    });
  }

  try {
    const response = await fetch(WEBHOOK_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData)
    });

    if (response.ok) {
      // Show success overlay
      const overlay = document.getElementById('successOverlay');
      overlay?.classList.add('show');
      form.reset();

      // Hide after 4 seconds
      setTimeout(() => {
        overlay?.classList.remove('show');
      }, 4000);
    } else {
      throw new Error('Server error');
    }
  } catch (error) {
    console.error('Error:', error);
    alert('Une erreur est survenue. Veuillez réessayer.');
  } finally {
    submitButton.disabled = false;
    buttonText.textContent = 'Envoyer ma demande';
    isSubmitting = false;
  }
};

// Setup scroll animations
const setupScrollAnimations = (): void => {
  const observerOptions: IntersectionObserverInit = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, observerOptions);

  document.querySelectorAll('.fade-in-section').forEach(el => {
    observer.observe(el);
  });
};

// Setup smooth scroll
const setupSmoothScroll = (): void => {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      e.preventDefault();
      const href = anchor.getAttribute('href');
      if (href) {
        const target = document.querySelector(href);
        target?.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
};

// Setup overlay click handler
const setupOverlayHandler = (): void => {
  const overlay = document.getElementById('successOverlay');
  overlay?.addEventListener('click', (e) => {
    if (e.target === overlay) {
      overlay.classList.remove('show');
    }
  });
};

// Initialize app
const init = (): void => {
  const app = document.getElementById('app');
  if (!app) return;

  // Render all sections
  app.innerHTML = `
    ${renderHero()}
    ${renderFeatures()}
    ${renderSuccessOverlay()}
  `;

  // Setup event listeners
  const form = document.getElementById('leadForm');
  form?.addEventListener('submit', handleFormSubmit);

  // Setup interactions
  setupScrollAnimations();
  setupSmoothScroll();
  setupOverlayHandler();
};

// Start app when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}